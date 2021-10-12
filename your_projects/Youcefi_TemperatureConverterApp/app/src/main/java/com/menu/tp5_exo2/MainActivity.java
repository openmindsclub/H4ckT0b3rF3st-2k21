package com.menu.tp5_exo2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

/**
 * Youcefi Nour Elhouda
 */

public class MainActivity extends AppCompatActivity {

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button mPasserelle = (Button) findViewById(R.id.button);
        mPasserelle.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                /** Le premier paramètre est le nom de l'activité actuelle
                 *Le second est le nom de l'activité de destination
                 **/
                Intent intent = new Intent(MainActivity.this, Main2Activity.class);
                // On lance l'intent
                startActivity(intent);
            }
        });
    }
}
