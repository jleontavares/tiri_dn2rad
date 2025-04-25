# tiri_dn2rad 
`jonathan.leontavares@vito.be
`
## 25April2025

`tiri_calibration_runner.py`  is a script to verify that our radiance estimates are consistent.

- Dependencies:
  - numpy
  - astropy
- DATA:
  - three selected observations
    - 'hera_tiri_20241010_201013_21_0_l1.fit'
    - 'hera_tiri_20241014_054521_31_0_l1.fit'
    - 'hera_tiri_20241018_223118_21_0_l1.fit'
  - Observed dark (slope and gain) based on data from **24Oct24**
  - Updated calibration coefficients (**LUT_BB+COLDBB_full_CASE42-44**) provided by Naoya.
- Remarks:
  - There are some (6) pixels for which the radiance is negative. Those pixels can be found as shown below:
    ```     
        np.where(radiance < 0)
  
        _Out[3]: (array([231, 245, 487, 550, 683, 734]), array([418, 222, 368, 499, 787, 879]))_
    ```
- OUTPUT:
  - The script prints out the mean and std of the radiance in the frame considered. My output is shown below:
  ```
    hera_tiri_20241010_201013_21_0_l1.fit
    Radiance mean: 3.408 +/- 0.777
    Radiance min: -121.145
    Radiance max: 42.493
    
    hera_tiri_20241014_054521_31_0_l1.fit
    Radiance mean: 3.510 +/- 0.663
    Radiance min: -118.216
    Radiance max: 35.356
    
    hera_tiri_20241018_223118_21_0_l1.fit
    Radiance mean: 3.414 +/- 0.648
    Radiance min: -118.924
    Radiance max: 37.308

```