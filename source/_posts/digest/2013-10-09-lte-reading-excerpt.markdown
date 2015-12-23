---
layout: post
title: "LTE reading excerpt"
date: 2013-10-09 18:21
comments: false
categories: Digest
tags:
- LTE
- writeup
- research
---

The LTE-Advanced introduced by LTE standard release 10 has many new features, including the carrier aggregation, enhanced intercell interferernce coordination (ICIC) for heterogeneous networks (HetNets), enhanced multiple-antenna transmission supporting up to eight downlink layers, and relaying and coordinated multipoint (CoMP) transmission.

For the carrier aggregation, in order to fully compliant with the IMT-Advanced requirements, the radio-access technology in LTE-Advanced does not only provide entensive support for deployment in spectrum allocations with bandwides ranging from 1 MHz to 20 MHz for backwards compatibility, but also extends by means of carrier aggregation, where multiple component carriers are aggregated and jointly used for transmission to/from a signle terminal. Up to five component carriers, possibly each of different bandwidth, can be aggregated, allowing for transmission bandwidth up to 100 MHz. The component carriers that a UE needs to support are determined through a UE-specific configuration process and a dynamic activation and deactivation process. Due to this activation/deactivation process, the state of SCells can be changed frequently. As a result, **radio link monitoring is only supported in the PCell but not in SCells to avoid complex UE behavior and additional control signaling overhead. Despite this kind of effort, the increased complexity due to physical downlink control channel (PDCCH) decoding and timing tracking of multiple component carriers cannot be avoided**. 

The receiver RF filter design depends on the type of carrier aggregation. For the interest of low hardware complexity, a singular RF chain is preferable. But it requires an analog-to-digital converter and RF filter with larger bandwidth. Moreover, due to activation and deactivation of component carriers, there is a retuning issue when a single RF is used for these component carriers. **There should be techniques balancing the packet loss due to RF retuning and the measurement of deactivated SCells to achieve optimal network performance**.

A HetNet consists of low-power picocells and femtocells in addition to high-power macrocells to improve end-users QoS. But this benefit comes at the cost of additional intercell interference between heterogeneous cells, and some of the femtocells might be closed subscriber group, which make the strongest downlink power at the viewpoint of certain UE be the interference. Besides, the commeon reference signal (CRS), synchronization signals, and physical broadcast channel (PBCH) are transmitted in almost blank subframe (ABS), which cause the collision among different Scells. **The interference cancellation should developed based on the release 8/9 which soly considers the macrocell interference management through ABS.

The LTE-Advanced system should fulfill the ITU requirements of the downlink peak spectral efficiency of 30 b/s/Hz. The peak spectral efficiency is the highest achievable data rate per overall cell bandwidth assuming error-free conditions when all available radio resources for the corresponding link direction are assigned to a single UE unit. While two- or four-layer transmission would be more prevalent even for the LTE-Advanced system, the required downlink peak spectral efficiency can only be attained using high-order antenna configurations (i.e., 8 × 8). **The main challenge of high-order multiple-input multiple-output (MIMO) is computational complexity**. Maximum likelihood (ML) detection is optimal in the sense that it minimizes error probability when the distributions of all data are equally likely. However, due to its high complexity in 8×8 MIMO systems with high modulation order, a direct implementation of ML detection might not be a viable option for such MIMO systems.

The alternatives are zero-forcing (ZF) and minimum mean square error (MMSE) detection, but both of them are much worse in performance compared with ML. The k-best detection is another choice, but although its performance is close to ML, its computational complexity is still high to be implemented in the real-world multi-antennas configurations.

In the UE, channel estimation is for feeding back channel state information (CSI) to the base station and equalization of the downlink channel in the process of data demodulation. One of the requirements for LTE-Advanced is that it should support up to eight-layer transmission, which implies that there need to be at least eight transmit antenna ports. Toward this, a key change in the reference signal design philosophy from LTE Release 8 is the separation of the demodulation reference signals (DM-RS) from the channel state information reference signals (CSI-RS) in Release 10. The up-side is saving significant reference signal overhead since it allows the densely populated DM-RS to be UE-specific. The down-side is that in order to provide for eight CSI-RS patterns, the density of CSI-RS in LTE-Advanced is significantly less than that of CRS, that is, there is only one CSI-RS resource element (RE) per RB per antenna port. Besides, CSI-RS is expected to be transmitted only once every five or ten sub-frames. **Advanced algorithms are needed for CSI-RS-based channel estimation and computation of the CSI feedback parameters such as CQI (i.e., modulation and coding rate) because existing methods may incur throughput degradation and/or result in a failure to meet the target BLER requirements.** Possible strategies to improve the CSI-RS channel estimation performance could include exploitation of the time-frequency correlations, the channel’s power delay profile (PDP) and the Doppler shift. 
  
  
  
[1] S. Parkvall, A. Furuskär, and E. Dahlman, "Evolution of LTE Toward IMT-Advanced," *IEEE Commun. Mag.*, vol. 49, no. 2, pp. 84-91, Feb, 2011.  
[2] D. Bai, C. Park, J. Lee, and H. Nguyen, "LTE-advanced modem design: challenges and perspectives," *IEEE Commun. Mag.*, vol. 50, no. 2, pp. 178-186, Feb. 2012.  
[3] E. Dahlman, S. Parkvall, and J. Sköld, *4G LTE/LTE-Advanced for Mobile Broadband*, Academic Press, 2011.  
[4] Z. Guo and P. Nilsson, "Algorithm and Implementation of the K-Best Sphere Decoding for MIMO Detection," *IEEE JSAC*, vol. 24, no. 3, Mar. 2006, pp. 491–503.  
[5] M. Baker, [LTE Advanced Physical Layer](http://www.3gpp.org/ftp/workshop/2009-12-17_ITU-R_IMT-Adv_eval/docs/pdf/REV-090003-r1.pdf).   
[6] J. Wannstrom, [Introduction to LTE-Advanced](http://www.3gpp.org/IMG/pdf/lte_advanced_v2.pdf).   


