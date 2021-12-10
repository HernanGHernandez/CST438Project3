package com.example.andriod_project3;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ParkingLotActivity extends AppCompatActivity {


    CardView A;
    CardView B;
    CardView C;
    CardView D;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.parking_lot);

        A = (CardView) findViewById(R.id.A);
        B = (CardView) findViewById(R.id.B);
        C = (CardView) findViewById(R.id.C);
        D = (CardView) findViewById(R.id.D);

        A.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(ParkingLotActivity.this, view_parking_lot.class);
                i.putExtra("lot", "A");
                startActivity(i);
            }
        });

        B.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(ParkingLotActivity.this, view_parking_lot.class);
                i.putExtra("lot", "B");
                startActivity(i);
            }
        });

        C.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(ParkingLotActivity.this, view_parking_lot.class);
                i.putExtra("lot", "C");
                startActivity(i);
            }
        });

        D.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent i = new Intent(ParkingLotActivity.this, view_parking_lot.class);
                i.putExtra("lot", "D");
                startActivity(i);
            }
        });
    }
}


