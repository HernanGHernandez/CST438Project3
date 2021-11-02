package com.example.andriod_project3;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class login extends AppCompatActivity {
    private EditText name, pass;
    private Button loginBtn,regBtn;
    String user = "123";
    String password = "321";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

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
                    Toast.makeText(login.this, "Username/Password input missing", Toast.LENGTH_LONG);
                }
                else if(userField == user && passField == password)
                {
                    Intent intent = new Intent(login.this, MainActivity.class);
                    startActivity(intent);
                }
            }
        });

    }
}
