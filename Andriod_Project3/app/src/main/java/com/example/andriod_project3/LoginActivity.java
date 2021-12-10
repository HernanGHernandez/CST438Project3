package com.example.andriod_project3;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import okhttp3.OkHttpClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class LoginActivity extends AppCompatActivity {
    // Layout pieces
    private EditText etUsername;
    private EditText etPassword;
    private Button buttonLogin;
    private Button createAcc;
    private List<User> users = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        etUsername = findViewById(R.id.username);
        etPassword = findViewById(R.id.password);
        buttonLogin = findViewById(R.id.loginBtn);
        createAcc = findViewById(R.id.regBtn);

        String API_BASE_URL = "http://park-res.herokuapp.com/";

        OkHttpClient.Builder httpClient = new OkHttpClient.Builder();

        IntentFactory factory = new IntentFactory();

        Retrofit.Builder builder =
                new Retrofit.Builder()
                        .baseUrl(API_BASE_URL)
                        .addConverterFactory(GsonConverterFactory.create());


        Retrofit retrofit =  builder.client(httpClient.build()).build();
        UserApi userApi = retrofit.create(UserApi.class);

        Call<List<User>> call = userApi.getUsers();

        call.enqueue(new Callback<List<User>>(){
            @Override
            public void onResponse(Call<List<User>> call, Response<List<User>> response) {
                if(!response.isSuccessful()){
                    Toast.makeText(LoginActivity.this, "Code: " + response.code(), Toast.LENGTH_SHORT).show();
                    return;
                }
                users = response.body();
            }

            @Override
            public void onFailure(Call<List<User>> call, Throwable t) {
                Log.d(String.valueOf(LoginActivity.this), t.getMessage());
                Toast.makeText(LoginActivity.this, "Error: " + t.getMessage(), Toast.LENGTH_SHORT).show();
            }
        });

        buttonLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String userName = etUsername.getText().toString();
                String passWord = etPassword.getText().toString();


                if(userName.isEmpty() || passWord.isEmpty()){
                    Toast.makeText(LoginActivity.this, "All fields required", Toast.LENGTH_SHORT).show();
                }else{
                    Toast.makeText(LoginActivity.this, "yooo", Toast.LENGTH_SHORT).show();
                    for (User user : users){
                        // If username exists
                        Toast.makeText(LoginActivity.this, "yesss", Toast.LENGTH_SHORT).show();
                        if(user.getUsername().equals(userName)){
                            if(user.getPassword().equals(passWord)){
                                Toast.makeText(LoginActivity.this, "Success", Toast.LENGTH_SHORT).show();
                                Intent intent = factory.getIntent(LoginActivity.this, ParkingLotActivity.class);
                                startActivity(intent);
                            }
                            else{
                                Toast.makeText(LoginActivity.this, "Password is incorrect", Toast.LENGTH_SHORT).show();
                            }
                        }else{
                            Toast.makeText(LoginActivity.this, "Username not found", Toast.LENGTH_SHORT).show();
                        }
                    }
                }
            }
        });

        createAcc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = factory.getIntent(LoginActivity.this, CreateAccountActivity.class);
                startActivity(intent);
            }
        });
    }
}