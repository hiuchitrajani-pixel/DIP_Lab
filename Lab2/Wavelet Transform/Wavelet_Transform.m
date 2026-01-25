clc;
clear all;
close all;


% Read input image
I = imread('D:\DIP_Images\lab2_part1.jpg');


% Rotate if required
% I = imrotate(I,90);


% Convert to grayscale
% Ig = rgb2gray(I);
Ig = I;


% Display original and grayscale image
figure;

subplot(2,3,1);
imshow(I);
title('Original Image');

subplot(2,3,2);
imshow(Ig);
title('Grayscale Image');


% Apply DWT using Haar wavelet
[Ia, Iv, Ih, Id] = dwt2(Ig,'haar');


% Convert for display
Ia = uint8(Ia);
Iv = uint8(Iv);
Ih = uint8(Ih);
Id = uint8(Id);


% Display DWT components
subplot(2,3,3);
imshow(Ia);
title('Approximation (LL)');

subplot(2,3,4);
imshow(Iv);
title('Vertical Detail (LH)');

subplot(2,3,5);
imshow(Ih);
title('Horizontal Detail (HL)');

subplot(2,3,6);
imshow(Id);
title('Diagonal Detail (HH)');


% Reconstruct image
I_recover = idwt2(Ia, Iv, Ih, Id, 'haar');
I_recover = uint8(I_recover);


% Display recovered image
figure;
imshow(I_recover);
title('Recovered Image');
