import numpy as np

def im2col(images, flt_h, flt_w, out_h, out_w, stride, pad):
    # バッチサイズ，チャンネル数，入力画像高さ，入力画像幅
    n_bt, n_ch, img_h, img_w = images.shape

    img_pad = np.pad(images, [(0,0), (0,0), (pad, pad), (pad, pad)], "constant")
    cols = np.zeros( (n_bt, n_ch, flt_h, flt_w, out_h, out_w) )

    for h in range(flt_h):
        h_lim = h + stride*out_h
        for w in range(flt_w):
            w_lim = w + stride*out_w
            cols[:, :, h, w, :, :] = images[:, :, h:h_lim*stride, w:w_lim*stride]
        # end for w
    # end for h

    cols = cols.transpose(1, 2, 3, 0, 4, 5).reshape(n_ch*flt_h*flt_w, n_bt*out_h*out_w)

    return cols



img = np.array( [[[[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]]]])
cols = im2col(img, 2, 2, 3, 3, 1, 0)
print(cols)

# [[ 1.  2.  3.  5.  6.  7.  9. 10. 11.]
#  [ 2.  3.  4.  6.  7.  8. 10. 11. 12.]
#  [ 5.  6.  7.  9. 10. 11. 13. 14. 15.]
#  [ 6.  7.  8. 10. 11. 12. 14. 15. 16.]]