import glob
from PIL import Image as PIL_Image
from images2gif import writeGif

gif_filename = 'studios-genres-MDS'
images = [PIL_Image.open(image) for image in glob.glob('images/'+gif_filename+'/*.png')]
file_path_name = 'images/' + gif_filename + '.gif'
writeGif(file_path_name, images, duration=0.2)
