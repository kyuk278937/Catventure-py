import CityScene
import HomeScene

class SceneManager():
    def run_scene(self,next_scene,screen):
        match next_scene:
            case 'city':
                CityScene.CityScene(screen)
            case 'home':
                HomeScene.HomeScene(screen,746)