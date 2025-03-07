import cv2
import tensorflow as tf
import numpy as np

def restore_corrupt_image(image_path, model_path="model/recovery_model.h5"):
    model = tf.keras.models.load_model(model_path)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128)) / 255.0
    img = np.expand_dims(img, axis=[0, -1])
    
    restored_img = model.predict(img)
    cv2.imwrite("restored.png", (restored_img[0] * 255).astype(np.uint8))
    print("Restoration complete. Saved as restored.png.")

if __name__ == "__main__":
    restore_corrupt_image("corrupt_image.png")
