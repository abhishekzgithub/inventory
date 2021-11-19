import React from "react";
import { ImageBackground, StyleSheet, View, Image, Text, SafeAreaView } from "react-native";


function ProductsScreen({navigaion}){
    return(
        <SafeAreaView>
            <ImageBackground
                    style={styles.background}
                    source={require("../assets/15Z_2102.w026.n002.163B.p1.163.jpg")}>
                    <View style={styles.logoContainer}>
                        <Image
                            style={styles.logo}
                            source={require("../assets/logo-red.png")}
                        ></Image>
                        <Text> Sell what you don't need. </Text>
                    </View>
                    
                    <View style={styles.loginButton}>
                    <Text> Email address </Text>
                    </View>
                    <View style={styles.registerButton}>
                    <Text> Phone Number </Text>
                    </View>
                    <View style={styles.registerButton}>
                        <Text> Password </Text>
                    </View>
                    <View style={styles.registerButton}>
                        <Text> Confirm Password </Text>
                    </View>
            </ImageBackground>
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