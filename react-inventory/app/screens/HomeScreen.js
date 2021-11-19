import React from "react";
import { ImageBackground, StyleSheet, View, Image, Button, TextInput, SafeAreaView } from "react-native";
import { BottomNavigation, Text } from 'react-native-paper';
import ProductScreen from "./inventory/ProductsScreen";

const MusicRoute = () => <Text>Cart</Text>;

const AlbumsRoute = () => <Text>Checkout</Text>;

const RecentsRoute = () => <Text>Profile</Text>;

const HomeScreen = () => {
  const [index, setIndex] = React.useState(0);
  const [routes] = React.useState([
    { key: 'music', title: 'Cart', icon: 'queue-music' },
    { key: 'albums', title: 'Checkout', icon: 'album' },
    { key: 'recents', title: 'Profile', icon: 'history' },
  ]);

  const renderScene = BottomNavigation.SceneMap({
    music: MusicRoute,
    albums: AlbumsRoute,
    recents: RecentsRoute,
  });

  return (
    <ProductScreen>
      {/* <BottomNavigation
      navigationState={{ index, routes }}
      onIndexChange={setIndex}
      renderScene={renderScene}
    /> */}
    </ProductScreen>
    
  );
};

export default HomeScreen;