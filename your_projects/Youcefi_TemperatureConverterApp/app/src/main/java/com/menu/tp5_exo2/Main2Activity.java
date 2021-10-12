package com.menu.tp5_exo2;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.TextView;

/**
 * Youcefi Nour Elhouda
 */

public class Main2Activity extends AppCompatActivity {
    private RadioButton mCelsiusRadio, mFahrenheitRadio;
    private Button mConvertir;
    private TextView mResultat;
    private EditText mValeur;
    private Float mNumber;

    private void init() {
        mValeur = findViewById(R.id.valeur);
        mConvertir = findViewById(R.id.btnConvertir);
        mCelsiusRadio=findViewById(R.id.ToCelsius);
        mFahrenheitRadio=findViewById(R.id.ToFahrenheit);
        mResultat=findViewById(R.id.resultat);
    }

    private boolean getValue() {

        if (!mValeur.getText().toString().isEmpty()) {

            mNumber = Float.valueOf(mValeur.getText().toString());
            return true;
        } else {
            AlertDialog.Builder builder = new AlertDialog.Builder(this);

            builder.setTitle("Erreur !")
                    .setPositiveButton("OK", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                        }
                    })
                    .setMessage("Un champ de saisi est vide")
                    .create()
                    .show();
            return false;
        }

    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        init();
        mConvertir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (getValue()) {
                    if (mCelsiusRadio.isChecked()) {
                        //Tc = (5/9)*(Tf-32)
                        float d1 = (float) 5 / 9;
                        float Tc = d1 * (mNumber - 32);
                        mResultat.setText(String.valueOf(Tc));
                    } else {
                        //Tf = (9/5)*Tc+32
                        float d2 = (float) 9 / 5;
                        float Tf = d2 * (mNumber + 32);
                        mResultat.setText(String.valueOf(Tf));
                    }
                }
            }
        });
    }
}
