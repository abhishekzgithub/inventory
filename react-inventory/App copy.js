import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View , FlatList} from 'react-native';
import  WelcomeScreen  from "./app/screens/WelcomeScreen";
import  LoginScreen  from "./app/screens/forms/LoginScreen";
import  RegisterScreen  from "./app/screens/forms/RegisterScreen";
import  HomeScreen  from "./app/screens/HomeScreen";
import DrawerMenu from "./app/screens/WelcomeScreen";

import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { DefaultTheme, Provider as PaperProvider } from 'react-native-paper';

const Stack = createNativeStackNavigator();
const Drawer = createDrawerNavigator();

function HomeScreen1({ navigation }) {  
  return (    
  <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>      
    <Button onPress={() => navigation.navigate('Notifications')} title="Go to notifications"      />    
  </View>  );
  }

function NotificationsScreen1({ navigation }) {  
  return (    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
                <Button onPress={() => navigation.goBack()} title="Go back home" />    </View>  )
          ;}

export default function App() {
  const theme = {
    ...DefaultTheme,
    colors: {
      ...DefaultTheme.colors,
      primary: 'tomato',
      accent: 'yellow',
    },
  };
  return (
    <PaperProvider theme={theme}>
      <NavigationContainer>
        <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Home" component={HomeScreen1} />
        <Drawer.Screen name="Notifications" component={NotificationsScreen1} />
          <Stack.Navigator>
            <Stack.Screen
              name="Welcome"
              component={WelcomeScreen}
              options={{ title: 'Welcome' }}>
            </Stack.Screen>
            <Stack.Screen
              name="Home"
              component={HomeScreen}
              options={{ title: 'Home' }}>
            </Stack.Screen>
            <Stack.Screen name="Login" component={LoginScreen} options={{ title: 'Login' }}/>
            <Stack.Screen name="Register" component={RegisterScreen} options={{ title: 'Register' }}/>
          </Stack.Navigator>
        </Drawer.Navigator>
      </NavigationContainer>
    </PaperProvider>

  );
  }