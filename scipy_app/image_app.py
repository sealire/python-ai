from scipy import misc

f = misc.face()
misc.imsave('face.png', f)  # uses the Image module (PIL)

face = misc.face(gray=False)
print(face.mean(), face.max(), face.min())
