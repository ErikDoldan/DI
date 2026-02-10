package com.example.aula.ui;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Button;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider;
import androidx.navigation.fragment.NavHostFragment;
import com.example.aula.R;
import com.example.aula.viewmodel.SettingsViewModel;
import com.example.aula.viewmodel.SettingsViewModelFactory;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.materialswitch.MaterialSwitch;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;


public class ProfileFragment extends Fragment {

    public ProfileFragment() {
        super(R.layout.fragment_profile);
    }
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState)
    {
        super.onViewCreated(view, savedInstanceState);
        TextView tvEmail = view.findViewById(R.id.tvUserEmail);
        Button btnVolver = view.findViewById(R.id.btnBackFromProfile);
        MaterialButton btnLogout2 = view.findViewById(R.id.btnLogout2);
        MaterialSwitch switchDark = view.findViewById(R.id.switchDarkMode);

        FirebaseUser user = FirebaseAuth.getInstance().getCurrentUser();
        if (user != null) {
            tvEmail.setText(user.getEmail());
        } else {
            tvEmail.setText("No hay sesión iniciada");
        }

        btnVolver.setOnClickListener(v -> {
            NavHostFragment.findNavController(this).popBackStack();
        });


        btnLogout2.setOnClickListener(v -> {
            FirebaseAuth.getInstance().signOut();
            NavHostFragment.findNavController(this)
                    .navigate(R.id.action_profile_to_authGate);
        });

        SettingsViewModelFactory settingsFactory = new SettingsViewModelFactory(requireContext());
        SettingsViewModel settingsVm = new ViewModelProvider(this, settingsFactory)
                .get(SettingsViewModel.class);


        settingsVm.getDarkMode().observe(getViewLifecycleOwner(), enabled -> {
            if (enabled == null) return;

            if (switchDark.isChecked() != enabled) {
                switchDark.setChecked(enabled);
            }

            AppCompatDelegate.setDefaultNightMode(
                    enabled ? AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO
            );
        });

        switchDark.setOnCheckedChangeListener((buttonView, isChecked) -> {
            settingsVm.setDarkMode(isChecked);
        });
    }
}
