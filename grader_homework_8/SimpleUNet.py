import torch
from torch import nn, Tensor
import math

class SinusoidalPositionEmbeddings(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim

    def forward(self, time: Tensor) -> Tensor:
        """
        time: (B)
        return: (B, dim)
        """
        device = time.device
        half_dim = self.dim // 2
        embeddings = math.log(10000) / (half_dim - 1)
        embeddings = torch.exp(torch.arange(half_dim, device=device) * -embeddings)
        embeddings = time[:, None] * embeddings[None, :]
        embeddings = torch.cat((embeddings.sin(), embeddings.cos()), dim=-1)
        return embeddings
    
class Block(nn.Module):
    def __init__(self, in_ch, out_ch, time_emb_dim):
        super().__init__()
        
        self.time_net = nn.Sequential(
            nn.Linear(time_emb_dim, out_ch),
            nn.ReLU()
        )
        self.net_1 = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, 1, 1),
            nn.ReLU(),
            nn.BatchNorm2d(out_ch),
        )
        self.net_2 = nn.Sequential(
            nn.Conv2d(out_ch, out_ch, 3, 1, 1),
            nn.ReLU(),
            nn.BatchNorm2d(out_ch),
        )
        
    def forward(self, x: Tensor, time_emb: Tensor) -> Tensor:
        time_emb = self.time_net(time_emb)
        time_emb = time_emb[:, :, None, None]
        time_emb = time_emb.expand(-1, -1, x.shape[2], x.shape[3])
        x = self.net_1(x)
        x = x + time_emb
        x = self.net_2(x)
        return x
    
class DownBlock(nn.Module):
    def __init__(self, in_ch, out_ch, time_emb_dim):
        super().__init__()
        self.block = Block(in_ch, out_ch, time_emb_dim)
        self.pool = nn.Conv2d(out_ch, out_ch, 4, 2, 1)

    def forward(self, x, time_emb):
        x = self.block(x, time_emb)
        pooled = self.pool(x)
        return pooled, x
    
class UpBlock(nn.Module):
    def __init__(self, in_ch, out_ch, time_emb_dim):
        super().__init__()
        self.block = Block(in_ch, out_ch, time_emb_dim)
        self.upsample = nn.ConvTranspose2d(in_ch, in_ch // 2, 4, 2, 1)

    def forward(self, x, skip, time_emb):
        x = self.upsample(x)
        x = torch.cat((x, skip), dim=1)
        x = self.block(x, time_emb)
        return x
    
class SimpleUNet(nn.Module):
    def __init__(self, time_emb_dim=32):
        super().__init__()
        self.time_emb = SinusoidalPositionEmbeddings(time_emb_dim)
        self.down1 = DownBlock(1, 32, time_emb_dim)
        self.down2 = DownBlock(32, 64, time_emb_dim)
        self.down3 = DownBlock(64, 128, time_emb_dim)
        self.mid = Block(128, 256, time_emb_dim)
        self.up1 = UpBlock(256, 128, time_emb_dim)
        self.up2 = UpBlock(128, 64, time_emb_dim)
        self.up3 = UpBlock(64, 32, time_emb_dim)
        self.out_conv = nn.Conv2d(32, 1, 1)

    def forward(self, x, t):
        """
        x: (B, 1, 28, 28)
        t: (B)
        return: (B, 1, 28, 28)
        """
        time_emb = self.time_emb(t)
        x, skip1 = self.down1(x, time_emb)
        x, skip2 = self.down2(x, time_emb)
        x, skip3 = self.down3(x, time_emb)
        x = self.mid(x, time_emb)
        x = self.up1(x, skip3, time_emb)
        x = self.up2(x, skip2, time_emb)
        x = self.up3(x, skip1, time_emb)
        x = self.out_conv(x)
        return x