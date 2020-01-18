
*****

# Command to train new data
# Default epochs = 4000

python scripts/retrain.py --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/space --bottleneck_dir=tf_files/bottlenecks 

*****

# Command to train new data
# Number of epochs = 500

python scripts/retrain.py --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=tf_files/space --how_many_training_steps=500 --bottleneck_dir=tf_files/bottlenecks 

*****

# Commands to test images to evaluate the trained model
# each line for each picture

python scripts/label_image.py --image astronaut_test_01.jpg
python scripts/label_image.py --image astronaut_test_02.jpg

python scripts/label_image.py --image airplane_test_01.jpg
python scripts/label_image.py --image airplane_test_02.jpg

python scripts/label_image.py --image cubesat_test_01.jpg
python scripts/label_image.py --image cubesat_test_02.jpg

python scripts/label_image.py --image earth_test_01.jpg
python scripts/label_image.py --image earth_test_02.jpg

*****