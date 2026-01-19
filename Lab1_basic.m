clc;
clear;
close all;

% Random 8x8 matrix (not used later, kept as in original code)
A = uint8(randi([0 255],8,8));

% Read image
I = imread('D:\DIP_Images\LAB1_pic.jpg');

% Show original image
figure;
imshow(I);
title('Original Image');

% Convert to grayscale
Ig = rgb2gray(I);

figure;
imshow(Ig);
title('Grayscale Image');

% Histogram equalization
Ieq = histeq(Ig);

figure;
imshow(Ieq);
title('Histogram Equalized Image');

% Convert grayscale to binary using threshold
bw = Ig > 128;

figure;
imshow(bw);
title('Black and White Image');

% Extract red channel
Ired = I;
Ired(:,:,2) = 0;
Ired(:,:,3) = 0;

figure;
imshow(Ired);
title('Red Channel Image');
