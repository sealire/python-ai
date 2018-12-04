from pyltp import Segmentor

model_path = "../ltp/cws.model"

seg = Segmentor()
seg.load(model_path)

words = seg.segment("你是那人间的四月天。")
print("| ".join(words))
