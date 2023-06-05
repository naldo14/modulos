import h5py
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def plot_data_from_h5py(h5py_file):
    global selected_data, selected_key

    if h5py_file == "/content/drive/MyDrive/tesis USB /Vibration, acoustic, temperature, and motor current dataset of rotating machine under varying operating conditions for fault diagnosis (korea)/vibration_1/vibration":
        with h5py.File(h5py_file, 'r') as h5_file:
            keys = list(h5_file.keys())

            print("Available files:")
            for i, key in enumerate(keys):
                print(f"{i+1}. {key}")

            file_index = int(input("Enter the index of the file you want to plot: ")) - 1
            if file_index < 0 or file_index >= len(keys):
                print("Invalid file index.")
                return

            selected_key = keys[file_index]
            selected_data = h5_file[selected_key][:]

            interactive = input("Do you want an interactive graph? (yes/no): ").lower()

            if interactive == 'yes':
                x = selected_data[:, 4]
                y1 = selected_data[:, 0]

                fig_1 = go.Figure(go.Scatter(x=x, y=selected_data[:, 0], mode='lines'))
                fig_1.update_layout(title='Amplitud de las vibraciones en el eje x (housing A) ' + selected_key,
                                    xaxis=dict(title='s'), yaxis=dict(title='g'))
                fig_1.show()

            else:
                fig, ax = plt.subplots(4, 1, figsize=(10, 10), sharex=True)

                ax[0].plot(selected_data[:, 4], selected_data[:, 0])
                ax[0].set_ylabel('g')
                ax[0].set_title('Amplitud de las vibraciones en el eje x (housing A) ' + selected_key)

                ax[1].plot(selected_data[:, 4], selected_data[:, 1])
                ax[1].set_ylabel('g')
                ax[1].set_title('Amplitud de las vibraciones en el eje y (housing A) ' + selected_key)

                ax[2].plot(selected_data[:, 4], selected_data[:, 2])
                ax[2].set_ylabel('g')
                ax[2].set_title('Amplitud de las vibraciones en el eje x (housing B) ' + selected_key)

                ax[3].plot(selected_data[:, 4], selected_data[:, 3])
                ax[3].set_ylabel('g')
                ax[3].set_xlabel('[s]')
                ax[3].set_title('Amplitud de las vibraciones en el eje y (housing B) ' + selected_key)

                plt.tight_layout()
                plt.show()
    else:
       with h5py.File(h5py_file, 'r') as h5_file:
        keys = list(h5_file.keys())

        print("Available files:")
        for i, key in enumerate(keys):
            print(f"{i+1}. {key}")

        file_index = int(input("Enter the index of the file you want to plot: ")) - 1
        if file_index < 0 or file_index >= len(keys):
            print("Invalid file index.")
            return

        selected_key = keys[file_index]
        selected_data = h5_file[selected_key][:]

        if "constant"in selected_key  and "normal" in selected_key:  # grafico de los dos housing , aqui grafico los archivos  vibration_normal_constant.csv: 
            time =np.linspace(0, 600, 15359999)
            fig, ax = plt.subplots(4, 1, figsize=(10, 10), sharex=True)

            ax[0].plot(time, selected_data[:, 0])
            ax[0].set_ylabel('g')
            ax[0].set_title('Amplitud de las vibraciones en el eje x (housing A) ' + selected_key)

            ax[1].plot(time, selected_data[:, 1])
            ax[1].set_ylabel('g')
            ax[1].set_title('Amplitud de las vibraciones en el eje y (housing A) ' + selected_key)

            ax[2].plot(time, selected_data[:, 2])
            ax[2].set_ylabel('g')
            ax[2].set_title('Amplitud de las vibraciones en el eje x (housing B) ' + selected_key)

            ax[3].plot(time, selected_data[:, 3])
            ax[3].set_ylabel('g')
            ax[3].set_xlabel('[s]')
            ax[3].set_title('Amplitud de las vibraciones en el eje y (housing B) ' + selected_key)

            plt.tight_layout()
            plt.show()
        elif  "constant"in selected_key: # en el housing A es donde esta la falla , aqui grafico los archivos vibration_inner/outer/ball_constant.csv
            time =np.linspace(0, 600, 15359999)
            fig, ax = plt.subplots(4, 1, figsize=(10, 10), sharex=True)

            ax[0].plot(time, selected_data[:, 0])
            ax[0].set_ylabel('g')
            ax[0].set_title('Amplitud de las vibraciones en el eje x (housing A) ' + selected_key)

            ax[1].plot(time, selected_data[:, 1])
            ax[1].set_ylabel('g')
            ax[1].set_title('Amplitud de las vibraciones en el eje y (housing A) ' + selected_key)

            ax[2].plot(time, selected_data[:, 2])
            ax[2].set_ylabel('g')
            ax[2].set_title('Amplitud de las vibraciones en el eje x (housing B) ' + selected_key)

            ax[3].plot(time, selected_data[:, 3])
            ax[3].set_ylabel('g')
            ax[3].set_xlabel('[s]')
            ax[3].set_title('Amplitud de las vibraciones en el eje y (housing B) ' + selected_key)

            plt.tight_layout()
            plt.show()

        if "0" in selected_key or  "1" in selected_key or "2" in selected_key or "3" in selected_key or "4" in selected_key or "5" in selected_key or "6" in selected_key:
            time =np.linspace(0, 300,7680000)
            fig, ax = plt.subplots(4, 1, figsize=(10, 10), sharex=True)

            ax[0].plot(time, selected_data[:, 0])
            ax[0].set_ylabel('g')
            ax[0].set_title('Amplitud de las vibraciones en el eje x (housing A) ' + selected_key)

            ax[1].plot(time, selected_data[:, 1])
            ax[1].set_ylabel('g')
            ax[1].set_title('Amplitud de las vibraciones en el eje y (housing A) ' + selected_key)

            ax[2].plot(time, selected_data[:, 2])
            ax[2].set_ylabel('g')
            ax[2].set_title('Amplitud de las vibraciones en el eje x (housing B) ' + selected_key)

            ax[3].plot(time, selected_data[:, 3])
            ax[3].set_ylabel('g')
            ax[3].set_xlabel('[s]')
            ax[3].set_title('Amplitud de las vibraciones en el eje y (housing B) ' + selected_key)

            plt.tight_layout()
            plt.show()



            

          





    
    
    