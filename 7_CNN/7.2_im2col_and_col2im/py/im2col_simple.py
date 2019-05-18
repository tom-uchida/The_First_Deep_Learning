import numpy as np

def im2col(image, flt_h, flt_w, out_h, out_w):
    img_h, img_w = image.shape # 入力画像の高さ，幅

    # 生成される行列のサイズ
    cols = np.zeros( (flt_h*flt_w, out_h*out_w) )

    for h in range(out_h):
        h_lim = h + flt_h
        for w in range(out_w):
            w_lim = w + flt_w
            cols[:,h*out_w+w] = image[h:h_lim, w:w_lim].reshape(-1)
        # end for w
    # end for h

    return cols



img = np.array( [   [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]])
cols = im2col(img, 2, 2, 3, 3)
print( cols )
# [[ 1.  2.  3.  5.  6.  7.  9. 10. 11.]
#  [ 2.  3.  4.  6.  7.  8. 10. 11. 12.]
#  [ 5.  6.  7.  9. 10. 11. 13. 14. 15.]
#  [ 6.  7.  8. 10. 11. 12. 14. 15. 16.]]