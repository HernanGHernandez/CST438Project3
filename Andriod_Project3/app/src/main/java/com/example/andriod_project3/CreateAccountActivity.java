package com.example.andriod_project3;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class CreateAccountActivity extends AppCompatActivity {
    private Button back_home;
    private Button create;
    private EditText etUsername;
    private EditText etPassword;
    private List<User> users;
    private boolean check = true;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_account);

        etUsername = findViewById(R.id.username);
        etPassword = findViewById(R.id.password);
        create = findViewById(R.id.button);
        back_home = findViewById(R.id.backk);

        back_home.setOnClickListener(v -> {
            Intent intent = new Intent(CreateAccountActivity.this, LoginActivity.class);
            startActivity(intent);
        });

        IntentFactory factory = new IntentFactory();

        create.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String user = etUsername.getText().toString();
                String pass= etPassword.getText().toString();

                Retrofit retrofit = new Retrofit.Builder()
                        .baseUrl("http://park-res.herokuapp.com/")
                        .addConverterFactory(GsonConverterFactory.create())
                        .build();
                UserApi userApi = retrofit.create(UserApi.class);
                Call<List<User>> call = userApi.getUsers();

                call.enqueue(new Callback<List<User>>(){
                    @Override
                    public void onResponse(Call<List<User>> call, Response<List<User>> response) {
                        if(!response.isSuccessful()){
                            Toast.makeText(CreateAccountActivity.this, "Code: " + response.code(), Toast.LENGTH_SHORT).show();
                            return;
                        }
                        users = response.body();
                        for (User p : users) {
                            if(p.getUsername().equals(user)){
                                check = false;
                                break;
                            }
                        }
                        if (check == true){
                            //Insert new user data into database here
                            postData(user, pass);
                            Toast.makeText(CreateAccountActivity.this, "Registered Successfully", Toast.LENGTH_SHORT).show();
                            Intent intent = factory.getIntent(CreateAccountActivity.this, LoginActivity.class);
                            startActivity(intent);
                        }else{
                            Toast.makeText(CreateAccountActivity.this, "Username already taken", Toast.LENGTH_LONG).show();
                            return;
                        }
                    }
                    @Override
                    public void onFailure(Call<List<User>> call, Throwable t) {
                        Toast.makeText(CreateAccountActivity.this, "Error: " + t.getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });

            }
        });
    }

    private void postData(String username, String password) {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://park-res.herokuapp.com/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        UserApi userApi = retrofit.create(UserApi.class);
        Call<Void> call = userApi.createUser(username, password);

        call.enqueue(new Callback<Void>(){
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                if(!response.isSuccessful()){
                    Toast.makeText(CreateAccountActivity.this, "Code: " + response.code(), Toast.LENGTH_SHORT).show();
                    return;
                }
            }
            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                Toast.makeText(CreateAccountActivity.this, "Error: " + t.getMessage(), Toast.LENGTH_LONG).show();
                System.out.println(t.getMessage());
            }
        });

    }
}