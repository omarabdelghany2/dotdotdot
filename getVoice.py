
import obsws_python as obs
import schedule
import time

class OBSController:
    def __init__(self):
        # OBS WebSocket Client
        self.SCENE1="SCENE1"
        self.SourceName="SOURCE1"
        self.client = obs.ReqClient(host='localhost', port=4444, password='password')
        





    # OBS control methods
    def obs_controller_original(self):
        x1 = self.client.get_scene_item_id(self.SCENE1, self.SourceName)
        scene_id1 = x1.scene_item_id
        self.client.set_scene_item_transform(self.SCENE1, scene_id1, {
            "boundsWidth": self.CAMERA_ORIGINAL_RESOLUTION_WIDTH,
            "sourceWidth": self.CANVAS_RESOLUTION_WIDTH,
            "boundsHeight": self.CAMERA_ORIGINAL_RESOLUTION_HEIGHT,
            "sourceHeight": self.CANVAS_RESOLUTION_HEIGHT,
            "boundsType":"OBS_BOUNDS_SCALE_INNER",
            "positionX": 0,
            "positionY": self.CANVAS_RESOLUTION_HEIGHT - self.CAMERA_ORIGINAL_RESOLUTION_HEIGHT
        })
    def print_hello(self):
         print("Hello")
         ##write in this function the code that will be used to click om on proprites





# Instantiate and start the OBSController
if __name__ == "__main__":

    controller = OBSController()
    schedule.every(1).hours.do(controller.print_hello)
    while True:
        # Run pending tasks
        schedule.run_pending()
        # Sleep for a while to prevent high CPU usage
        time.sleep(1)
    # controller.obs_controller_original()









