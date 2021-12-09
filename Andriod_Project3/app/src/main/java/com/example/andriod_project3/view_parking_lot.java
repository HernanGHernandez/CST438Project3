package com.example.andriod_project3;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class view_parking_lot extends AppCompatActivity implements lotViewAdapter.OnItemClickListener {
    private RecyclerView mRecyclerview;
    private lotViewAdapter mLotViewAdapter;
    private ArrayList<lotModel> mLotModels;
    private RequestQueue mRequestQueue;
    String lot= "A";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_parking_lot);

        mRecyclerview = findViewById(R.id.recycler_view);
        mRecyclerview.setHasFixedSize(true);
        mRecyclerview.setLayoutManager(new LinearLayoutManager(this));
        mRequestQueue = Volley.newRequestQueue(this);
        mLotModels=new ArrayList<>();
        parseJSON(lot);
    }

    private void parseJSON(String lot) {
        String url= "https://parkresapp.herokuapp.com/getLot" +lot+"/?format=json";
        JsonArrayRequest request= new JsonArrayRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONArray>() {
                    @Override
                    public void onResponse(JSONArray response) {
                        for(int i=0; i< response.length();i++){
                            try {
                                JSONObject space = response.getJSONObject(i);
                                int userID=space.getInt("userId");
                                int spaceNum=space.getInt("space");
                                boolean taken=space.getBoolean("takenBool");
                                int lotId=space.getInt("LotAId");

                                mLotModels.add(new lotModel(lotId,spaceNum,taken,userID));
                            } catch (JSONException e) {
                                e.printStackTrace();
                            }

                        }
                        mLotViewAdapter=new lotViewAdapter(view_parking_lot.this,mLotModels);
                        mRecyclerview.setAdapter(mLotViewAdapter);
                        mLotViewAdapter.setOnItemClickListener(view_parking_lot.this);

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                error.printStackTrace();
            }
        });
        mRequestQueue.add(request);
    }

    @Override
    public void onItemClick(int position) {
        lotModel data=mLotModels.get(position);
        int lotId=data.getLotId();
        String urlupdate="https://parkresapp.herokuapp.com/updateParkingLot"+lot+"/"+lotId;

        StringRequest request= new StringRequest(Request.Method.PUT, urlupdate,new Response.Listener<String>(){
            @Override
            public void onResponse(String s) {
                Toast.makeText(view_parking_lot.this, "Data Updated..", Toast.LENGTH_SHORT).show();
            }
        },new Response.ErrorListener(){
            @Override
            public void onErrorResponse(VolleyError volleyError) {
                Toast.makeText(view_parking_lot.this, "error", Toast.LENGTH_SHORT).show();
            }
        })
        {
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                Map<String, String> parameters = new HashMap<String, String>();
                //parameters.put("takenBool", "true");
                parameters.put("LotAId",String.valueOf(lotId));
                parameters.put("space",String.valueOf(data.getSpace()));
                parameters.put("takenBool", "true");
                parameters.put("userId", String.valueOf(data.getUserId()));
                return parameters;
            }
        };
        mRequestQueue.add(request);

    }
}