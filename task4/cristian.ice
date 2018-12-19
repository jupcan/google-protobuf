module ssdd {
  interface Cristian {
    double getServerTime(string dni, double tc1);
  };
  interface SyncReport {
    void notifyTime(string dni, string fullname, double newTime, double error, double tc2);
  };
};
