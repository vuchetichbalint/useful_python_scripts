from PIL import Image

def get_ratio(w,h,w0,h0):
	# it resizes to maximum 640*360pxs
	if w < w0 and h < h0:
		return w,h
	if w < w0:
		return w*h0//h, h0
	if h < h0:
		return w0, h*w0//w
	
	if (w//w0 < h//h0):
		return w*h0//h, h0
	else:
		return w0, h*w0//w

def resize_rational(file):
	w0 = 640
	h0 = 360
	
	im = Image.open(file)
	if im.size[0] < w0 and im.size[1] < h0:
		return
	
	im = im.resize(get_ratio(im.size[0], im.size[1], w0, h0), Image.ANTIALIAS)
	# see docs: http://effbot.org/imagingbook/image.htm#tag-Image.Image.size
	im.save(file)

if __name__ == "__main__":
	resize_rational('img/thankyouforyourattention0.png')