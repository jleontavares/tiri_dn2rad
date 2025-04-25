import numpy as np
from astropy.io import fits


def load_fits(fname):
    hdu_list = fits.open(fname, do_not_scale_image_data=False)
    data = hdu_list[0].data
    the_header = hdu_list[0].header
    return np.float32(data), the_header


if __name__ == '__main__':
    selected_files = ['hera_tiri_20241010_201013_21_0_l1.fit',
                      'hera_tiri_20241014_054521_31_0_l1.fit',
                      'hera_tiri_20241018_223118_21_0_l1.fit']

    for file in selected_files:
        cfg = {'obs_fname': file,
               'slope_obs_dark': 'SLOPE_DARK_MODEL_2024-10-24_filter_g.fit',
               'offset_obs_dark': 'OFFSET_DARK_MODEL_2024-10-24_filter_g.fit',
               'slope_calibration': 'LUT_fil-1_slope.fit',
               'offset_calibration': 'LUT_fil-1_intercept.fit',
               }

        dn_array, dn_header = load_fits(cfg['obs_fname'])
        slope_obs_dark_array, _ = load_fits(cfg['slope_obs_dark'])
        offset_obs_dark_array, _ = load_fits(cfg['offset_obs_dark'])

        dark_array = slope_obs_dark_array * dn_header['CAS_TEMP'] + offset_obs_dark_array

        dn_minus_dark = dn_array - dark_array

        slope_calibration, _ = load_fits(cfg['slope_calibration'])
        offset_calibration, _ = load_fits(cfg['offset_calibration'])

        slope_calibration = np.where(slope_calibration < 1e-5, np.nan, slope_calibration)

        radiance = (dn_minus_dark - offset_calibration) / slope_calibration

        print(file)
        print(f'Radiance mean: {np.nanmean(radiance):.3f} +/- {np.nanstd(radiance):.3f}')
        print(f'Radiance min: {np.nanmin(radiance):.3f}')
        print(f'Radiance max: {np.nanmax(radiance):.3f}')
        print('')
