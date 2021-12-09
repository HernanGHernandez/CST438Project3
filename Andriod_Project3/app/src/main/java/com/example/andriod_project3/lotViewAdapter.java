package com.example.andriod_project3;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class lotViewAdapter extends RecyclerView.Adapter<lotViewAdapter.lotViewHolder> {

    private Context mContext;
    private ArrayList<lotModel> mLotModels;
    private OnItemClickListener mListener;

    public interface OnItemClickListener{
        void onItemClick(int position);
    }

    public lotViewAdapter(Context context, ArrayList<lotModel> lotModels){
        mContext=context;
        mLotModels=lotModels;
    }
    public void setOnItemClickListener(OnItemClickListener listener){
        mListener=listener;
    }

    @NonNull
    @Override
    public lotViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
       View v= LayoutInflater.from(mContext).inflate(R.layout.lot_model,parent,false);
       return new lotViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull lotViewHolder holder, int position) {
        lotModel currentItem=mLotModels.get(position);

        int spaceNumber=currentItem.getSpace();
        int userID=currentItem.getUserId();
        boolean isTaken=currentItem.isTakenBool();

        holder.mSpaceNumber.setText("Space Number: "+ String.valueOf(spaceNumber));
        holder.mIsTaken.setText("Reserved: "+String.valueOf(isTaken));

    }

    @Override
    public int getItemCount() {
        return mLotModels.size();
    }

    public class lotViewHolder extends RecyclerView.ViewHolder{

        public TextView mSpaceNumber;
        public TextView mIsTaken;
        public TextView mUserID;

        public lotViewHolder(@NonNull View itemView) {
            super(itemView);
            mSpaceNumber=itemView.findViewById(R.id.space);
            mIsTaken=itemView.findViewById(R.id.taken);
            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if(mListener!=null){
                        int position =getAdapterPosition();
                        if (position!= RecyclerView.NO_POSITION){
                            mListener.onItemClick(position);
                        }
                    }
                }
            });
        }

    }
}
