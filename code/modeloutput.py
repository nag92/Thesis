from Vicon.Mocap import Vicon
file = "path to CSV file"
data = Vicon.Vicon(file)
model = data.get_model_output()
model.left_leg().hip.angle.x
