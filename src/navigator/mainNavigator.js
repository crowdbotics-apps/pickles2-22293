import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import NotificationList2181102Navigator from '../features/NotificationList2181102/navigator';
import Maps3181101Navigator from '../features/Maps3181101/navigator';
import SignIn21167503Navigator from '../features/SignIn21167503/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
NotificationList2181102: { screen: NotificationList2181102Navigator },
Maps3181101: { screen: Maps3181101Navigator },
SignIn21167503: { screen: SignIn21167503Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
