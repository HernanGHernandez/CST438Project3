package com.example.andriod_project3;

import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface user {
    @Headers( "Content-Type: application/json" )
    @POST("login/")
    Call<person> login(@Body JsonObject login);
}