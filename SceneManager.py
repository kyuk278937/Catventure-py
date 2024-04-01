import CityScene
import HomeScene
import ShopScene

class SceneManager():
    def run_scene(self,next_scene,screen,bias_x = 0):
        match next_scene:
            case 'city':
                CityScene.CityScene(screen, bias_x)
            case 'home':
                HomeScene.HomeScene(screen, bias_x)
            case 'shop':
                ShopScene.ShopScene(screen, bias_x)