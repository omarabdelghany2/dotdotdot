import obsws_python as obs
import schedule
import time

class OBSController:
    def __init__(self):
        # OBS WebSocket Client
        self.SCENE1 = "SCENE1"  # Example scene name
        self.SourceName = "SOURCE1"  # Example source name
        self.client = obs.ReqClient(host='localhost', port=4444, password='password')

    # Method to fetch all scenes and their scene item IDs
    def get_scenes(self):
        scenes = self.client.get_scene_list()  # Retrieve all scenes
        for scene in scenes.scenes:
            print(f"Scene Name: {scene['sceneName']}, Scene Index: {scene['sceneIndex']}")

    # OBS control methods
    def obs_controller_original(self):
        print("Entered here")
        # Get scene item ID
        x1 = self.client.get_scene_item_id(self.SCENE1, self.SourceName)
        scene_id1 = x1.scene_item_id
        print(f"Scene Item ID for {self.SourceName}: {scene_id1}")
        
        # Get the current transform data
        transform_response = self.client.get_scene_item_transform(self.SCENE1, scene_id1)
        transform = transform_response.scene_item_transform  # Extract the transform dictionary
        print(f"Transform data: {transform}")
        # Remove the 'boundsWidth' from the transform dictionary
        if 'boundsWidth' in transform:
            del transform['boundsWidth']
        if 'boundsHeight' in transform:
            del transform['boundsWidth']
        
        # Ensure the transform is serialized properly before passing it
        if isinstance(transform, dict):
            # Pass the correct arguments without 'scene_item_id', instead 'sceneItemId'
            self.client.set_scene_item_transform(self.SCENE1,scene_id1,transform)
        else:
            print("Transform is not in the correct format.")
            return


# Instantiate and start the OBSController
if __name__ == "__main__":
    controller = OBSController()
    # Print all scene UUIDs
    controller.get_scenes()  # Fetch scene list and UUIDs

    # Schedule the task to run every 1 minute
    schedule.every(2).seconds.do(controller.obs_controller_original)
    
    while True:
        # Run pending tasks
        schedule.run_pending()
        # Sleep for a while to prevent high CPU usage
        time.sleep(1)
