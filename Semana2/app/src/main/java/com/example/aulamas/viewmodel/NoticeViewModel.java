package com.example.aulamas.viewmodel;

import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;
import androidx.lifecycle.ViewModel;
import com.example.aulamas.data.NoticeRepository;
import java.util.List;
public class NoticeViewModel extends ViewModel {




        private final NoticeRepository repository = new NoticeRepository();

        // Estado 1: El texto con todos los avisos
        private final MutableLiveData<String> _textOutput = new MutableLiveData<>();
        // Estado 2: ¿Está la lista vacía? (Para mostrar/ocultar el mensaje de "Sin avisos")
        private final MutableLiveData<Boolean> _isEmpty = new MutableLiveData<>(true);
        public void deleteNotice(String content) {
            repository.removeNotice(content);
            refreshData(); // Actualizamos la pantalla para que desaparezca
        }
        public LiveData<String> getTextOutput() { return _textOutput; }
        public LiveData<Boolean> isListEmpty() { return _isEmpty; }

        // Al iniciar, cargamos lo que haya
        public NoticeViewModel() {
            refreshData();
        }

        public void addNotice(String content) {
            repository.addNotice(content);
            refreshData();
        }

        private void refreshData() {
            List<String> all = repository.getAllNotices();

            // 1. Actualizamos si está vacío o no
            _isEmpty.setValue(all.isEmpty());

            // 2. Formateamos la lista para mostrarla
            StringBuilder sb = new StringBuilder();
            for (String s : all) {
                sb.append("• ").append(s).append("\n\n");
            }
            _textOutput.setValue(sb.toString());
        }
    }

