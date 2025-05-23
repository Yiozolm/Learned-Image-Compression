# About This Repo

A personal review to existing Learned Image Compression (LIC) Methods. 

### Listed Models

#### Before Straight-Through Estimator(STE)
- [x] [Factorized](http://arxiv.org/pdf/1802.01436) **ICLR2018**
- [x] [Hyperprior](http://arxiv.org/pdf/1802.01436) **ICLR2018** Scale-Only Hyperprior
- [x] [Mbtmean-2018](http://arxiv.org/pdf/1809.02736) **NurIPS2018** Mean+Scale Hyperprior
- [x] [Mbt2018](http://arxiv.org/pdf/1809.02736) **NurIPS2018** Mean+Scale+Context Hyperprior
- [x] [SGA2020](http://arxiv.org/pdf/2006.04240) **NeurIPS 2020** SGA Guided Hyperprior
- [x] [Cheng2020Anchor](http://arxiv.org/pdf/2001.01568) **CVPR2020** Gaussian Mixture Model
- [x] [Cheng2020Attn](http://arxiv.org/pdf/2001.01568) **CVPR2020** Gaussian Mixture Model
- [x] [InvCompress](https://dl.acm.org/doi/10.1145/3474085.3475213) **ACM MM2021** Invertible Encoder/Decoder
- [ ] [Informer](https://openaccess.thecvf.com/content/CVPR2022/html/Kim_Joint_Global_and_Local_Hierarchical_Priors_for_Learned_Image_Compression_CVPR_2022_paper.html) **CVPR2022** Joint Global and Local Hyperpriors
- [x] [DPICT2022](https://ieeexplore.ieee.org/document/9879330/) **CVPR2022** Fine Granular Scalability

#### After Straight-Through Estimator(STE)
- [ ] [minnen2020](https://ieeexplore.ieee.org/document/9190935/) **ICIP2020** LRP & STE
- [ ] [Cheng2020AnchorCheckBoard](http://arxiv.org/pdf/2103.15306) **CVPR2021** CheckBoard Parallel Acceleration for Cheng2020Model
- [ ] [Entroformer2022](http://arxiv.org/pdf/2202.05492) **ICLR2022** Transformer-Based Entropy Model
- [x] [ELIC2022](http://arxiv.org/pdf/2203.10886) **CVPR2022** SCCTX 
- [x] [WACNN2022](https://ieeexplore.ieee.org/document/9878760/) **CVPR2022** Two Type of Encoder/Decoder (**CNN**)
- [x] [STF2022](https://ieeexplore.ieee.org/document/9878760/) **CVPR2022** Two Type of Encoder/Decoder (**Transformer**)
- [x] [TCM2023](https://ieeexplore.ieee.org/document/10204195/) **CVPR2023** Mixture of CNN and Transformer
- [x] [MLIC2023](https://dl.acm.org/doi/10.1145/3581783.3611694) **ACM MM2023** Multi Reference Entropy Model
- [x] [CCA2024](https://arxiv.org/pdf/2410.04847) **NurIPS2024** Auxiliary Loss
- [x] [WeConvene](http://arxiv.org/pdf/2407.09983) **ECCV2024** Add Wavelet Transform into TCM2023
- [x] [FLIC2024](http://arxiv.org/pdf/2501.13751) **ICLR2024** Multi-Scale Directional Frequency Decomposition
- [ ] [MambaIC2025](https://arxiv.org/pdf/2503.12461) **CVPR2025** Integrate Mamba into Hyper Encoder/Decoder
- [x] [LALIC2025](https://arxiv.org/pdf/2502.05741) **CVPR2025** RMKV into LIC
- [ ] [DCAE2025](https://arxiv.org/pdf/2504.00496) **CVPR2025** Dictionary-based Cross Attention Module

#### Other
- [x] [STanH](http://arxiv.org/pdf/2410.00557) **TIP** Tanh Quantization

---
### Update Log
- **2025-3-27:** The Progress on Entroformer is quite slow due to original code is really hard to use 
- **2025-3-28:** Add `STanH` `LALIC2025` into repo
- **2025-4-6:** Add `DCAE2025` into repo
---
### Evaluation
Some evaluation results on [Kodak](https://r0k.us/graphics/kodak/) Dataset are available in this repo.

The used checkpoint files are obtained from both [Compressai](https://github.com/InterDigitalInc/CompressAI) and author repos.

#### Detailed Configuration
1. Single **RTX A4000 GPU** is used to evaluate the models.
2. `python==3.8.10` `torch==1.11.0` `cuda==113` `pytorch_msssim==1.0.0` `pytorch_fid==0.3.0` `lpips==0.1.4` `DISTS_pytorch==0.1`

### Related Links
* Unofficial Minnen2020 Implement: https://github.com/tokkiwa/minnen2020
* Unofficial ELIC2022 ReImplement: https://github.com/VincentChandelier/ELiC-ReImplemetation
* WACNN2022 & STF2022 official Repo: https://github.com/Googolxx/STF
* TCM2023 official Repo: https://github.com/jmliu206/LIC_TCM
* MLIC2023 Series official Repo: https://github.com/JiangWeibeta/MLIC
* CCA2024 official Repo: https://github.com/LabShuHangGU/CCA
* WeConvene official Repo: https://github.com/fengyurenpingsheng/WeConvene
* FLIC2024 official Repo: https://github.com/qingshi9974/ICLR2024-FTIC
* MambaIC2025 official Repo: https://github.com/AuroraZengfh/MambaIC
* STanH official Repo: https://github.com/EIDOSLAB/StanH
* LALIC2025 official Repo: https://github.com/sjtu-medialab/RwkvCompress