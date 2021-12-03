package com.example.andriod_project3;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class create_account extends AppCompatActivity {
    private Button back_home;
    private Button create;
    private EditText username;
    private EditText password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_account);
        username = findViewById(R.id.User);
        password = findViewById(R.id.create_password);
        create = findViewById(R.id.button);
        back_home = findViewById(R.id.backk);

        back_home.setOnClickListener(v -> {
            Intent intent = new Intent(create_account.this, login.class);
            startActivity(intent);
        });
        create.setOnClickListener(v -> {
            Retrofit.Builder builder = new Retrofit.Builder()
                    .baseUrl("http://park-res.herokuapp.com/")
                    .addConverterFactory(GsonConverterFactory.create());
            Retrofit retrofit = builder.build();
            user account = retrofit.create(user.class);
            String new_user = username.getText().toString();
            String new_pass = password.getText().toString();
            Call < person > new_person = account.create(new_user, new_pass);
            new_person.enqueue(new Callback < person > () {
                @Override
                public void onResponse(Call < person > call, Response < person > response) {
                    Intent intent = new Intent(create_account.this, login.class); // takes you back to main because I dont know what to put instead
                    startActivity(intent);
                }

                @Override
                public void onFailure(Call < person > call, Throwable t) {
                    alert("creation failed");
                    Log.e("create_account failed", t.toString());
                }
            });

        });
    }
    private void alert(String message) {
        AlertDialog dlg = new AlertDialog.Builder(create_account.this)
                .setTitle("Error")
                .setMessage(message)
                .setPositiveButton("ok", (dialog, which) -> dialog.dismiss())
                .create();
        dlg.show();
    }
}