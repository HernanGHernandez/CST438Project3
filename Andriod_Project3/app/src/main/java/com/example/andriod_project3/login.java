package com.example.andriod_project3;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class login extends AppCompatActivity {
    private EditText name, pass;
    private Button loginBtn,regBtn;
    String user = "123";
    String password = "321";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        name = findViewById(R.id.username);
        pass = findViewById(R.id.password);

        loginBtn = findViewById(R.id.loginBtn);
        regBtn = findViewById(R.id.regBtn);


        // register button
        regBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(login.this, create_account.class);
                startActivity(intent);
            }
        });
        loginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // doesnt work the pop up message aint doing its job
                String userField = name.getText().toString();
                String passField = pass.getText().toString();

                if (userField.isEmpty() && passField.isEmpty()) {
                    alert("No Password nor Username was entered");
                }
                else if(userField.equals(user) && passField.equals(password))
                {
                    Intent intent = new Intent(login.this, MainActivity.class);// takes you back to main because I dont know what to put instead
                    startActivity(intent);
                }
            }
        });

    }
    private void alert(String message)
    {
        AlertDialog dlg = new AlertDialog.Builder(login.this)
                .setTitle("Error")
                .setMessage(message)
                .setPositiveButton("ok", (dialog, which) -> dialog.dismiss())
                .create();
        dlg.show();
    }
}
