clc;
clear all;
close all;


% Read image
I = imread("D:\DIP_Images\Lab2_part3.jpeg");


% Get size
[m, n] = size(I);


% -------------------------------
% Bit Plane Slicing
% -------------------------------

for ii = 1:m
    for jj = 1:n

        Bitp0(ii,jj) = bitand(I(ii,jj),1)   > 0;
        Bitp1(ii,jj) = bitand(I(ii,jj),2)   > 0;
        Bitp2(ii,jj) = bitand(I(ii,jj),4)   > 0;
        Bitp3(ii,jj) = bitand(I(ii,jj),8)   > 0;
        Bitp4(ii,jj) = bitand(I(ii,jj),16)  > 0;
        Bitp5(ii,jj) = bitand(I(ii,jj),32)  > 0;
        Bitp6(ii,jj) = bitand(I(ii,jj),64)  > 0;
        Bitp7(ii,jj) = bitand(I(ii,jj),128) > 0;

    end
end


% -------------------------------
% Bit Plane Removal
% -------------------------------

for ii = 1:m
    for jj = 1:n

        bitpr0(ii,jj) = bitand(I(ii,jj),255-(2^0));
        bitpr5(ii,jj) = bitand(I(ii,jj),255-(2^5));
        bitpr7(ii,jj) = bitand(I(ii,jj),255-(2^7));

    end
end


% -------------------------------
% Display (Single Window)
% -------------------------------

figure;


subplot(3,4,1);
imshow(I);
title('Org');


subplot(3,4,2);
imshow(Bitp0);
title('B0');

subplot(3,4,3);
imshow(Bitp1);
title('B1');

subplot(3,4,4);
imshow(Bitp2);
title('B2');


subplot(3,4,5);
imshow(Bitp3);
title('B3');

subplot(3,4,6);
imshow(Bitp4);
title('B4');

subplot(3,4,7);
imshow(Bitp5);
title('B5');

subplot(3,4,8);
imshow(Bitp6);
title('B6');


subplot(3,4,9);
imshow(Bitp7);
title('B7');

subplot(3,4,10);
imshow(bitpr0);
title('R0');

subplot(3,4,11);
imshow(bitpr5);
title('R5');

subplot(3,4,12);
imshow(bitpr7);
title('R7');
