// by weld
// - fft (let python do it?) ---> yes
// - ddm 

#include <complex.h>
#include <math.h>
#include <stdio.h>
#include <omp.h>

typedef double _Complex cmplx;

void computeDDM(int number_images,
                int width, int height,
                cmplx* fft, double* ddm,
                int number_delays, int* indexdelays) {

    // utils
    int imagesize = width * height;
    int fftsize = imagesize * number_images;
    int ddmsize = imagesize * number_delays;

    for(int i = 0; i < ddmsize; i++)
        ddm[i] = 0.0;


    #pragma omp parallel for schedule(nonmonotonic:dynamic)
    for(int idelay = 0; idelay < number_delays; idelay++) {
        int t,pix;

        // shortcut ptrs
        const cmplx  *i1, *i2;
        double* ddm_current_frame = &ddm[idelay * imagesize];

        // update of ddm averages
        for(t = indexdelays[number_delays - 1]; t < number_images; t++) {
           
            i1 = &fft[t * imagesize];
            i2 = &fft[(t - indexdelays[idelay]) * imagesize];

            for(pix = 0; pix < imagesize ; pix++) {
                ddm_current_frame[pix] +=
                    pow(creal(i1[pix] - i2[pix]), 2.) +
                    pow(cimag(i1[pix] - i2[pix]), 2.);

            }
        }
    }
    
    float mean_weight = 1. / (2 * imagesize * (number_images - number_delays));
    for(int i = 0; i < ddmsize ; i++)
        ddm[i] *= mean_weight;
}
