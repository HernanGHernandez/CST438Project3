package com.example.andriod_project3;

public class lotModel {
    private int lotId;
    private int space;
    private boolean takenBool;
    private int userId;


    public lotModel(int lotId, int space, boolean takenBool, int userId){
        this.userId=userId;
        this.lotId=lotId;
        this.space=space;
        this.takenBool=takenBool;
    }

    public int getLotId() {
        return lotId;
    }

    public void setLotId(int lotId) {
        this.lotId = lotId;
    }

    public int getSpace() {
        return space;
    }

    public void setSpace(int space) {
        this.space = space;
    }

    public boolean isTakenBool() {
        return takenBool;
    }

    public void setTakenBool(boolean takenBool) {
        this.takenBool = takenBool;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }
}
