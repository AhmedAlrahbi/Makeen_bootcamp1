#ICA_1 block,gap counting
x = 0
fullWidth = int(input("Enter width?  "))

WidthPercolor = fullWidth / 2

blockWidth = 5

widthBlack = (WidthPercolor / blockWidth) 
widthWhite = WidthPercolor / blockWidth - 1

gap = (WidthPercolor - widthWhite * blockWidth )  

print(round(widthBlack), round(widthWhite), gap)
