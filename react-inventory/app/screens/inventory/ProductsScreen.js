import React from "react";
import { ImageBackground, StyleSheet, View, Image, Text, SafeAreaView, FlatList } from "react-native";
import plants from "../../consts/plants";


function ProductsScreen({navigation}){
    return(
        <SafeAreaView>
            <View >
                <Text> Plant1 </Text>
                <Image
                ></Image>
            </View>
            <View >
                <Text> Plant2 </Text>
            </View>
            <View >
                <Text> Plant3 </Text>
            </View>
            <View >
                <Text> Plant4 </Text>
            </View>
            <View >
                <Text> Plant5 </Text>
            </View>
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    background:{
        flex: 1,
        justifyContent:"flex-end",
        alignItems:"center"
        
    },
    loginButton:{
        width:"100%",
        height: 70,
        backgroundColor:"#fc5c65"
    },
    registerButton:{
        width:"100%",
        height: 70,
        backgroundColor:"#4ecdc4"
    },
    logo:{
        width:"100px",
        height:"100px",
        position:"relative",
        left: "10px"
    },
    logoContainer:{
        position:"relative",
        alignItems:"center",
        bottom: "410px",
    }
})

export default ProductsScreen;