package com.example.andriod_project3;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

import org.json.JSONException;
import org.json.JSONObject;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class login extends AppCompatActivity {
    private EditText name, pass;
    private Button loginBtn, regBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        name = findViewById(R.id.username);
        pass = findViewById(R.id.password);

        loginBtn = findViewById(R.id.loginBtn);
        regBtn = findViewById(R.id.regBtn);

        regBtn.setOnClickListener(v -> {
            Intent intent = new Intent(login.this, create_account.class);
            startActivity(intent);
        });
        loginBtn.setOnClickListener(v -> {
            Retrofit.Builder builder = new Retrofit.Builder()
                    .baseUrl("http://parkresapp.herokuapp.com/")
                    .addConverterFactory(GsonConverterFactory.create());
            Retrofit retrofit = builder.build();

            user user1 = retrofit.create(user.class);
            String userField = name.getText().toString();
            String passField = pass.getText().toString();

            Call < login_class > logining = user1.login(userField, passField);
            logining.enqueue(new Callback < login_class > () {
                @Override
                public void onResponse(Call < login_class > call, Response < login_class > response) {
                    Intent intent = new Intent(login.this, MainActivity.class); // takes you back to main because I dont know what to put instead
                    startActivity(intent);
                }
                @Override
                public void onFailure(Call < login_class > call, Throwable t) {
                    alert("login failed");
                }
            });

        });
    }

    private void alert(String message) {
        AlertDialog dlg = new AlertDialog.Builder(login.this)
                .setTitle("Error")
                .setMessage(message)
                .setPositiveButton("ok", (dialog, which) -> dialog.dismiss())
                .create();
        dlg.show();
    }
}