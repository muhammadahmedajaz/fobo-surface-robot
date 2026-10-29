%% HYDROBOT LCS MODEL AND CONTROLLER

% Simple heading (yaw) model: Psi(s)/Tau(s) = K / [ s (T s + 1) ]
K = 0.5;     % DC gain (depends on thruster distance and inertia)
T = 0.8;     % time constant (depends on drag and inertia)

num = [K];
den = [T 1 0];     % (T s + 1) * s = T s^2 + s

sys = tf(num, den);

%% 1) Open-loop step response (NO controller)
figure;
step(sys);
grid on;
title('Open-Loop Step Response (Heading vs Torque input)');
xlabel('Time (s)');
ylabel('Heading \psi (rad)');

%% 2) Design a PID controller for heading
Kp = 3.0;
Ki = 0.8;
Kd = 0.4;

C = pid(Kp, Ki, Kd);

%% 3) Closed-loop system with unity feedback
sys_cl = feedback(C*sys, 1);

figure;
step(sys_cl);
grid on;
title('Closed-Loop Step Response with PID (Desired heading step)');
xlabel('Time (s)');
ylabel('Heading \psi (rad)');

%% 4) Bode plot (for LCS stability discussion)
figure;
bode(sys);
grid on;
title('Open-Loop Bode Plot of Heading Dynamics');

%% 5) Disturbance test (optional)
% Model disturbance as extra torque added at plant input:
% Here we just show a response to disturbance using step on plant
t = 0:0.1:20;
dist_torque = zeros(size(t));
dist_torque(t>5) = 0.3;   % at t>5s, a constant torque disturbance

[y, t_out] = lsim(sys_cl, dist_torque, t);

figure;
plot(t_out, y, 'LineWidth', 1.5);
grid on;
title('Closed-Loop Response to Disturbance Torque');
xlabel('Time (s)');
ylabel('Heading \psi (rad)');
%% Root Locus with PID gains marked
figure;
rlocus(C*sys);
grid on;
title('Root Locus with Current PID Gains');

% Compute closed-loop poles with current PID
sys_cl = feedback(C*sys,1);
poles_cl = pole(sys_cl);

% Mark closed-loop poles on root locus
hold on;
plot(real(poles_cl), imag(poles_cl), 'rx', 'MarkerSize', 10, 'LineWidth', 2);
legend('Root Locus','Closed-loop Poles');
%% 4) Bode plot (for LCS stability discussion)
figure;
bode(sys);
grid on;
title('Open-Loop Bode Plot of Heading Dynamics');


