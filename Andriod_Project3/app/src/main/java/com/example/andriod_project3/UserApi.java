package com.example.andriod_project3;

import com.google.gson.JsonObject;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.Headers;
import retrofit2.http.POST;

//public interface user {
//    @Headers( "Content-Type: application/json" )
//    @POST("login/")
//    Call<login_class> login(@Field("username")String name, @Field("password") String password);
//    @Headers( "Content-Type: application/json" )
//    @POST("createUser/")
//    Call<person> create(@Field("username")String user, @Field("password")String pass);
//}

public interface UserApi {
    // Note this relative url must match the API
    // "posts" is for testing purposes

    @GET("allUsers")
    Call<List<User>> getUsers();

//    @FormUrlEncoded
//    @POST("createUser")
//    Call<Void> createUser(@Field("name") String name, @Field("password") String password);

    @FormUrlEncoded
    @POST("createUser")
    Call<Void> createUser(@Field("username") String username, @Field("password") String password);
}
