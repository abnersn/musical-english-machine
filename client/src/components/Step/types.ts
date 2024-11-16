import React from 'react';

export type StepProps = {
  title: string;
  complete: boolean;
  error: boolean;
} & React.PropsWithChildren;
