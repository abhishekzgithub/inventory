import React from "react";
import { ImageBackground, StyleSheet, View, Image, Text, Button, TextInput, SafeAreaView } from "react-native";


function LoginScreen({navigation}){
    const [text, onChangeText] = React.useState("Please input here.");

    return(
        <ImageBackground
            style={styles.background}
            source={require("../../assets/15Z_2102.w026.n002.163B.p1.163.jpg")}>
            <View style={styles.logoContainer}>
                <Image
                    style={styles.logo}
                    source={require("../../assets/logo-red.png")}
                ></Image>
                <Text> Sell what you don't need. </Text>
            </View>
            
            <SafeAreaView style={styles.loginButton}>
                <Text> Email address </Text>
                <TextInput
                    onChangeText={onChangeText}
                    value={text}
                />
            </SafeAreaView>
            <SafeAreaView style={styles.loginButton}>
                <Text> Password </Text>
                <TextInput
                    onChangeText={onChangeText}
                    value={text}
                />
            </SafeAreaView>
            <View style={styles.registerButton}>
                <Button
                    title="Login"
                    onPress={() =>
                        navigation.navigate('Home', { name: 'Jane' })
                        }
                > Register </Button>
            </View>
        </ImageBackground>
        
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

export default LoginScreen;