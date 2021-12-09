package com.example.andriod_project3;
import com.google.gson.annotations.SerializedName;


public class Parking {
    private int userId;
    private int parkingId;
    private String slot;
    private String lot;
    private boolean parkSwitch;

    @SerializedName("body")
    private String text;

    public Parking(int userId, int parkingId, String slot, String lot, boolean parkSwitch) {
        this.userId = userId;
        this.parkingId = parkingId;
        this.slot = slot;
        this.lot = lot;
        this.parkSwitch = parkSwitch;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public int getParkingId() {
        return parkingId;
    }

    public void setParkingId(int parkingId) {
        this.parkingId = parkingId;
    }

    public String getSlot() {
        return slot;
    }

    public void setSlot(String slot) {
        this.slot = slot;
    }

    public String getLot() {
        return lot;
    }

    public void setLot(String lot) {
        this.lot = lot;
    }

    public boolean isParkSwitch() {
        return parkSwitch;
    }

    public void setParkSwitch(boolean parkSwitch) {
        this.parkSwitch = parkSwitch;
    }
}