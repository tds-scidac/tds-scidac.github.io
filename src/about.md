## About TDS

Our Center is supported by the SciDAC program of the U.S. Department
of Energy, jointly funded by the Office of Fusion Energy Sciences (FES) and
the Office of Advanced Scientific Computing Research (ASCR).

----

## Our Team 

{% set members = ['X_Tang', 'J_Shadid', 'O_Beznosov', 'J_Bonilla', 'a_boozer', 'J_Burby', 'TanBui', 'P_Cagas', 
'L_Chacon', 'HK_Chung', 'J_Colgan', 'e_constantinescu', 'm_crockatt', 'BenDudson',
'H_Elman', 'C_Fontes', 'N_Garland', 'Z_Guo', 'Hamilton', 'z_jorti', 'I_Keramidas', 'T_kolev', 'NamiLi', 'Y_Li', 'K_Lipnikov', 'H_Mao', 'R_Maulik',   
'C_McDevitt',  'M_Picklo', 'J_Rudi', 'P_Sharma', 'B_Srinivasan', 'E_Startsev', 'Q_Tang', 'WX_Wang', 'T_Wildey', 'G_Wimmer', 			
  'XQXu', 'M_Yoo', 'M_Zammit', 'Y_Zhang', 'B_Zhu'] %}

{% for member in members %}
<div class="row">
    <div class="col-md-2">
        <img src="../bios/{{ member }}.jpg" alt="Missing picture" width="100%">
    </div>
    <div class="col-md-10">
        <br><p>
        {% set bio = "/bios/" + member + ".html" %}
            {% include bio %}
        </p>
    </div>
</div>
{% endfor %}

----

## Alumni

{% set members = ['JianGuoChen', 'S_Conde', 'M_Ding', 'K_Huang', 'Shinhoo_Kang', 'J_Li', 'S_Liu',
'ChenhaoMa', 'Sriram_M', 'Z_Peng', 'A_Rappaport', 'B_Shen', 'LiboWang'] %}

{% for member in members %}
<div class="row">
    <div class="col-md-2">
        <img src="../bios/{{ member }}.jpg" alt="Missing picture" width="100%">
    </div>
    <div class="col-md-10">
        <br><p>
        {% set bio = "/bios/" + member + ".html" %}
            {% include bio %}
        </p>
    </div>
</div>
{% endfor %}
