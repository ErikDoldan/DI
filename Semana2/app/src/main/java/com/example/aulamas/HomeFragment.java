package com.example.aulamas;

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.lifecycle.ViewModelProvider; // Importante para MVVM
import androidx.navigation.fragment.NavHostFragment;

import com.example.aulamas.R;
import com.example.aulamas.viewmodel.NoticeViewModel;
import com.google.android.material.button.MaterialButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.textfield.TextInputEditText;
import com.google.android.material.textfield.TextInputLayout;

public class HomeFragment extends Fragment {

    public HomeFragment() {
        super(R.layout.fragment_home);
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // 1. Instanciar ViewModel (Mantiene los datos vivos)
        NoticeViewModel viewModel = new ViewModelProvider(this).get(NoticeViewModel.class);

        // 2. Referencias UI
        TextInputEditText etAviso = view.findViewById(R.id.etAviso);
        TextInputLayout tilAviso = view.findViewById(R.id.tilAviso);
        MaterialButton btnGuardar = view.findViewById(R.id.btnGuardar);
        TextView tvListado = view.findViewById(R.id.tvListado);
        TextView tvEmpty = view.findViewById(R.id.tvEmpty);
        MaterialButton btnLogout = view.findViewById(R.id.btnLogout);


        btnLogout.setOnClickListener(v -> {
            // 1. Cerrar sesión en Firebase
            com.google.firebase.auth.FirebaseAuth.getInstance().signOut();

            // 2. Navegar al Gate para reiniciar el flujo
            NavHostFragment.findNavController(this).navigate(R.id.action_home_to_gate);
        });
        // 3. OBSERVAR DATOS (Reactividad)

        // A) Actualizar la lista de texto
        viewModel.getTextOutput().observe(getViewLifecycleOwner(), texto -> {
            tvListado.setText(texto);
        });

        // B) Mostrar/Ocultar mensaje de vacío (Cumple Práctica 2)
        viewModel.isListEmpty().observe(getViewLifecycleOwner(), vacio -> {
            if (vacio) {
                tvEmpty.setVisibility(View.VISIBLE);
                tvListado.setVisibility(View.GONE);
            } else {
                tvEmpty.setVisibility(View.GONE);
                tvListado.setVisibility(View.VISIBLE);
            }
        });

        // 4. EVENTO CLICK
        btnGuardar.setOnClickListener(v -> {
            String texto = etAviso.getText().toString();

            if (texto.isEmpty()) {
                tilAviso.setError("Escribe algo primero");
            } else {
                tilAviso.setError(null);

                // 1. AÑADIR (Acción normal)
                viewModel.addNotice(texto);
                etAviso.setText("");

                // 2. SNACKBAR CON "DESHACER" REAL
                Snackbar.make(view, "Aviso añadido", Snackbar.LENGTH_LONG)
                        .setAction("DESHACER", view1 -> {
                            // Si pulsa deshacer, lo borramos del ViewModel
                            viewModel.deleteNotice(texto);
                        })
                        .show();
            }

        });
    }
}