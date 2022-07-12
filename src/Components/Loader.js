import React from 'react';
import { Stack } from '@mui/material';
import SyncLoader from "react-spinners/SyncLoader";

const Loader = () => (
  <Stack direction="row" justifyContent="center" alignItems="center" width="100%">
    <SyncLoader color="#9A1212" />
  </Stack>
);

export default Loader;